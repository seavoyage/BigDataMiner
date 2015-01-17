#MRJob

pip intall mrjob

from mrjob.job import MRJob

class SimpleWordCOunt(MRJob):

    def mapper(self, _, line):
        for word in line.split(" "):
            yield (word.lower(), 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    SimpleWordCount.run()

# Inline
python word_count.py muchado.txt

# Local
python word_count.py muchado.txt -r local

#EMR
python word_count.py muchado.txt -r emr --conf-path=mrjob,conf

runners:
    emr:
        aws_access_key_id <YOUR AWS KEY>
        aws_region;us-east-1'
        aws_secret_access_key <YOUR SECRET ACCESS KEY>
        aws_instance_type c1.xlarge
        nun_ec2-instances: 8
