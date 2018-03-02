# read-daly  
Read and Show [DALY Dataset](http://thoth.inrialpes.fr/daly/)  
> DALY - Daily Action Localization in Youtube videos - is intended for research in action recognition. It is suitable to train and test temporal/spatial localization algorithms.

## Demo  
<img src="/samples/rg3Mr6e1KMo_sample.gif" width="600">

## Usage

#### Basic
```
> python read-daly.py
```

###### Arguments  
> -n, --videoNumber = Get specific number of video  
> -r, --randomVideo = Get random Video  
> -s, --saveVideo = Save result as avi format  

###### Example
```
> python read-daly.py -r 1 -s 1
```
> Get random video, and save result as avi format

```
> python read-daly.py -n 10
```
> Get 10th video, and just show it's result

## Dependencies

Install
- Python 3.6.4
- numpy 1.14.0
- opencv-python 3.4.0.12
- ...

## Reference

### Citation
    @article{DBLP:journals/corr/WeinzaepfelMS16,
      author    = {Philippe Weinzaepfel and
                   Xavier Martin and
                   Cordelia Schmid},
      title     = {Towards Weakly-Supervised Action Localization},
      journal   = {CoRR},
      volume    = {abs/1605.05197},
      year      = {2016}
    }
