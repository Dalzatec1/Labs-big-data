from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        vector = line.split(',')
        sector=vector[1]
        employ=vector[2]
        yield sector,employ

    def reducer(self, key, values):
        prom=list(values)
        
        yield key, prom

if __name__ == '__main__':
    MRWordFrequencyCount.run()