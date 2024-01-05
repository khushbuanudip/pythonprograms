class Python:
    class_topic_python="Constant"
    def python_method(self):
        print("this is topic of python")
class Java:
    class_topic_java="variable"
    def python_method(self):
        print("this is topic of java")

class Subject(Java,Python):
      class_subject="Both java and python"
obj_sub = Subject()
obj_sub.python_method()
#obj_sub.java_method()
print(obj_sub.class_topic_python)
