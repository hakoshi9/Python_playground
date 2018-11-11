"""クラス変数"""
# クラス変数は、「他のオブジェクトでも共有される変数」
# 通常、そのクラス内で使いたい変数は初期化時に生成する
# クラスをインスタント化したときに生成され、それはそのクラス独自に持つことができる
# しかしクラス変数は、そのクラスを使って生成されたインスタンス間で値が共有される

class Person(object):
    kind = 'human'
    job_opportunities = []

    def __init__(self, name='unknown'):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

    def add_job_opportunities(self, job):
        self.job_opportunities.append(job)


a = Person('A')
a.who_are_you()

b = Person('B')
b.who_are_you()

a.add_job_opportunities('Programmer')
print(a.job_opportunities)
b.add_job_opportunities('Police Officer')
print(b.job_opportunities)