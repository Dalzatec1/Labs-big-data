from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
#       for w in line.decode('utf-8', 'ignore').split():
        vector = line.split(',')
        sector=vector[1]
        salary= int(vector[2])
        yield sector,salary

    def reducer(self, key, values):
        listAux=list(values)
        prom=sum(listAux)/len(listAux)
        yield key, prom

if __name__ == '__main__':
    MRWordFrequencyCount.run()