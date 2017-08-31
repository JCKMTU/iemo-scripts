# mocap_data_analysis
Collection of data analysis

## Mocap data
### By sessions: 


| Session | Total_frame | Noise | Num_files |
| ------- | ----------- | ----- | --------- |
| 1 | 953394 | 22.2% | 28 |
| 2 | 925384 | 1.5% | 30 |
| 3 | 1043520 | 3.0% | 32 |
| 4 | 1007705 | 22.8% | 30 |
| 5 | 1013412 | 63.9% | 30 |

### By emotions:


| Emotion | Total_frame | Noise | Num_files |
| ----------- | ----------- | ----- | --------- | 
| anger | 589083 | 24.6% | 1090 |
| happiness | 307145 | 20.9% | 586 |
| sadness | 708802 | 19.2% | 1077 |
| neutral | 796835 | 23.0% | 1704 |
| frustrated | 1030800 | 22.5% | 1829 |
| excited | 596650 | 29.2% | 1041 |
| fearful | 13069 | 24.9% | 40 |
| disgusted | 562 | 45.5% | 2 |
| surprise | 39245 | 20.9% | 105 |
| other | 1802 | 2.0% | 3 |
| undefined | 1235115 | 25.3% | 2472 |

## Problems
The problems that have to be solved
 - Mostly unusable Session 5 dataset. 
 - Gap filling, smoothing algorithm for data with noises.
 - Some of the files are present in 'dialog' session but absent in 'sentences' session

The data is taken by VICON motion capture system which has a gap filling/interporation feature to eliminate NaN values. However, the data has to be trimmed manually frame by frame without using VICON's proprietary software, mobu, neural net, or something else. 