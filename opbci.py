from pylsl import StreamInlet, resolve_stream
import numpy as np
import time
def saveData():
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    # create a new inlet to read from the stream
    listTimestamp = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    lenght_data = 5000
    nb_data = 0
    inlet = StreamInlet(streams[0])
    n_sample = 0
    while True:
        begin = int(time.clock() * 1000)
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        # append the sample of timestamp and each channel to the list
        listTimestamp.append(timestamp)
        c1.append(sample[0])
        c2.append(sample[1])
        c3.append(sample[2])
        c4.append(sample[3])
        c5.append(sample[4])
        c6.append(sample[5])
        c7.append(sample[6])
        c8.append(sample[7])
        nb_data += 1
        # save when there is 5000 timestamps
        if nb_data > lenght_data:
            # reset the number of data
            nb_data = 0
            # save in CSV
            all_data = [listTimestamp, c1, c2, c3, c4, c5, c6, c7, c8]
            np.savetxt("sample" + str(n_sample) + ".csv", np.asarray(all_data), delimiter=",")
            # reset
            listTimestamp = []
            c1 = []
            c2 = []
            c3 = []
            c4 = []
            c5 = []
            c6 = []
            c7 = []
            c8 = []
            n_sample += 1
        end = int(time.clock()*1000)
        print(end - begin)
saveData()