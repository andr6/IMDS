import config
import cPickle as pickle
import Analyzers

def callback(ch, method, properties, body):
    dbody = pickle.loads(body)
    print 'Received: ', dbody[0]
    filepath = config.NFS_LOCAL_PATH + dbody[0]

    #Yara Analyze
    print "Signature Matching..."
    yar = Analyzers.YaraAnalyzer(filepath)
    yar.doAnalyze()
    yar_score = yar.getScore()
    yar_result = yar.getResult()

    #Static Analyze
    print "Static Analysis..."
    stc = Analyzers.StaticAnalyzer(filepath)
    src.doAnalyze()
    src_score = src.getScore()
    src_result = src.getResult()

    #Dynamic Analyze
    print "Dynamic Analysis..."
    dyn = Analyzers.CuckooAnalyzer(filepath)
    dyn.doAnalyze()
    dyn_score = dyn.getScore()
    dyn_result = dyn.getResult()

    #Sending Results to Server
    print "Sending Results to Server..."

    #Sending Ack to RabbitMQ
    print "Sending Ack..."
    ch.basic_ack(delivery_tag = method.delivery_tag)

    print "Done."
