#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
   Training part of the Deep QA model
   
"""

from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 Xuming Lin. All Rights Reserved"
__author__    = "Xuming Lin"
__date__      = "2017-08-21:23:42:17"


from qacnn import QACNN
import tensorflow as tf
import datetime
import operator
import data

# Config函数
class Config(object):
    def __init__(self, vocab_size):
        # 输入序列(句子)长度
        self.sequence_length = 200
        # 循环数
        self.num_epochs = 100000
        # batch大小
        self.batch_size = 100
        # 词表大小
        self.vocab_size = vocab_size
        # 词向量大小
        self.embedding_size = 100
        # 不同类型的filter,相当于1-gram,2-gram,3-gram和5-gram
        self.filter_sizes = [1, 2, 3, 5]
        # 隐层大小
        self.hidden_size = 80
        # 每种filter的数量
        self.num_filters = 512
        # 论文里给的是0.0001
        self.l2_reg_lambda = 0.
        # dropout
        self.keep_prob = 1.0
        # 学习率
        # 论文里给的是0.01
        self.lr = 0.01
        # margin
        # 论文里给的是0.009
        self.m = 0.05
        # 设定GPU的性质,允许将不能在GPU上处理的部分放到CPU
        # 设置log打印
        self.cf = tf.ConfigProto(allow_soft_placement=True, log_device_placement=False)
        # 只占用20%的GPU内存
        self.cf.gpu_options.per_process_gpu_memory_fraction = 0.2


print('Loading Data...')

# 词映射ID
vocab = data.vocab_data

# 配置文件
config = Config(len(vocab['word2id']))


# 开始训练和测试
with tf.device('/gpu:0'):
    with tf.Session(config=config.cf) as sess:
        # 建立CNN网络
        cnn = QACNN(config, sess)
        # 训练函数
        def train_step(x_batch_1, x_batch_2, x_batch_3):
            feed_dict = {
                cnn.q: x_batch_1,
                cnn.aplus: x_batch_2,
                cnn.aminus: x_batch_3,
                cnn.keep_prob: config.keep_prob
            }
            _, step, loss, accuracy = sess.run(
                [cnn.train_op, cnn.global_step, cnn.loss, cnn.accu],
                feed_dict)
            time_str = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
        # 测试函数
        def dev_step():
            scoreDict = dict()
            for qids, x_test_1, x_test_2, labels in data.load_valid(config.batch_size, config.sequence_length, config.sequence_length):
                feed_dict = {
                    cnn.q: x_test_1,
                    cnn.aplus: x_test_2,
                    cnn.aminus: x_test_2,
                    cnn.keep_prob: 1.0
                }
                batch_scores = sess.run(cnn.q_ap_cosine, feed_dict)
                for score, qid, label in zip(batch_scores, qids, labels):
                    scoreDict.setdefault(qid, list)
                    scoreDict[qid].append([score, label])
            lev1 = .0
            lev0 = .0
            for k, v in scoreDict.items():
                v.sort(key=operator.itemgetter(0), reverse=True)
                score, flag = v[0]
                if flag == '1':
                    lev1 += 1
                if flag == '0':
                    lev0 += 1
            # 回答的正确数和错误数
            print('回答正确数 ' + str(lev1))
            print('回答错误数 ' + str(lev0))
            print('准确率 ' + str(float(lev1)/(lev1+lev0)))

        # 每5000步测试一下
        evaluate_every = 5000
        # 开始训练和测试
        sess.run(tf.global_variables_initializer())
        for i in range(config.num_epochs):
            for (_, x_batch_1, x_batch_2, x_batch_3) in data.load_train(config.batch_size, config.sequence_length, config.sequence_length):
                train_step(x_batch_1, x_batch_2, x_batch_3)
                if (i+1) % evaluate_every == 0:
                    print("\n测试{}:".format((i+1)/evaluate_every))
                    dev_step()
                    print

