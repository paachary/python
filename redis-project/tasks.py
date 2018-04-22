from flask import Flask, render_template, request, redirect
import redis


application = Flask(__name__)

r = redis.Redis()


@application.route('/',methods=['GET'])
def get_tasks():
    keyval = get_info()

    tasks = r.lrange('tasks',0,-1)

    return render_template('index.html',tasks_list = tasks,
                                        len_task = len(tasks),
                                        keyval = keyval)


@application.route('/tasks/delete',methods=['POST'])
def delete_tasks():
    selected_task = request.form.getlist("tasks")
    tasks = r.lrange('tasks',0,-1)
    for counter in selected_task:
        r.lrem('tasks', tasks[int(counter)])

    return redirect("/")


@application.route('/tasks/add',methods=['POST'])
def add_tasks():
    try:
        task = request.form['task']

        if task==None or len(task) == 0:
            raise ValueError('Task cannot be NULL')

        r.lpush('tasks', task)
        return redirect("/")

    except ValueError as error:
        print('Caught this error: ' + repr(error))
        return redirect("/")


@application.route('/personal/update',methods=['POST'])
def upd_info():
    try:
        keys = r.hkeys('user')
        for key in keys:
            val = request.form[key.decode("utf-8")]
            if (val == None or len(val) == 0 ):
                raise ValueError('Values cannot be NULL')
            r.hset('user',key, val)
        return redirect("/")

    except ValueError as error:
        print('Caught this error: ' + repr(error))
        return redirect("/")


def get_info():
    keyval = {}
    keys = r.hkeys('user')
    for key in keys:
        val = r.hget('user', key)
        keyval[key] = val
    return keyval


if (__name__ == '__main__'):
    application.run(host='localhost', port=5050)
