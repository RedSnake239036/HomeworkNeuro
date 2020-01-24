import tensorflow as tf # в дальнейшем эта строка будет опускаться
# #плейсхолдеры - тензоры, значение в которых не получается в результате выполнения операций над другими тензорами, а задается извне
# #Переменные - значения элементов этих тензоров подбираются в процессе обучения нейронной сети
# #Значения других тензоров в определенном смысле остаются неизменными
# #Тензоры мат.операций - это стандартный вид тензора, в большом количестве возможно неявно присутствующий в любой нейронной сети
#deprecated - Осуждаю
# x = tf.Variable(tf.zeros([10, 10]), name = 'x')
# x = tf.get_variable('x', [2, 3])
# y = tf.get_variable('y', [2, 3], dtype=tf.int32, initializer=tf.zeros_initializer)
# z = tf.get_variable('z', dtype=tf.int32, initializer=tf.constant([10, 20]))
#
# plsh = tf.placeholder(dtype=tf.int32, shape=None, name='Stay')
# sloj = tf.add(t1, t2)

x = tf.get_variable('x', initializer=tf.random_normal((2, 2)))
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(x))
sess.close


a = tf.constant([[1, 1], [2, 2], [3, 3]])
b = tf.constant([[1, 2], [3, 4]])
c = tf.matmul(a, b)
with tf.Session() as sess:
    print(c.eval())


a = tf.placeholder(float, shape=[3, 2])# создание плейсхолдеров с размерностью
b = tf.placeholder(float, shape=[2, 2])
c = tf.matmul(a, b) #умножение матриц
print(c.eval(
    feed_dict={
        a: [[1, 1], [2, 2], [3, 3]],
        b: [[1, 2], [3, 4]]
    },
    session=tf.Session()
)) #передача значений словаря напрямую в метод и выполнение с выводом на экран, в сессии
#loss = tf.reduce(tf.square(y-y_pred))
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred, labels=y))

optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
session.run([optimizer, loss], feed_dict=feed_dict)


