from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        vector = line.split(',')
        empleado=vector[1]
        salario= int(vector[2])
        yield empleado,salario

    def reducer(self, key, values):
        lista=list(values)
        prom=sum(lista)/len(lista)
        yield key, prom

if __name__ == '__main__':
    MRWordFrequencyCount.run()