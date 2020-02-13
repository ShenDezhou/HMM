#A Simple Hidden Markov Model based Chinese Word Segmentation Project.

为了得到HMM模型，可根据如下步骤进行：  
1.利用中文序列、序列对应状态计算转移矩阵，发射矩阵；    
2.实现Viterbi算法，估计中文序列对应状态。  

In order to obtain the HMM model, the transfer matrix can be calculated by using the Chinese sequence, the sequence corresponding state, the emission matrix, 2. the Viterbi algorithm is realized to estimate the corresponding state of the Chinese sequence.  

#1. Estimate Transfer Matrix and Emission Matrix
首先，计算转移矩阵、发射矩阵。将Second International Chinese Word Segmentation Bakeoff标注语料pku_training，去重得到4700字的pku_char_dict，利用hmmestimate训练得到转移矩阵T和发射矩阵E。  
  
First, the transfer matrix and the emission matrix are calculated. Label the Second International Chinese Word Segmentation Bakeoff pku_training to get a 4,700-word pku_char_dict. The transfer matrix T and the emission matrix E are obtained by the training of hmmestimate.    

#2. Viterbi: finds the optimal hidden state sequence of the observation sequence.
接着，实现Viterbi算法。利用转移矩阵和发射矩阵作为HMM模型，计算一个中文序列的潜在状态序列。  

Next, the Viterbi algorithm is implemented. Using the transfer matrix and the emission matrix as the HMM model, the potential state sequence of a Chinese sequence is calculated.    

![Viterbi](https://pic2.zhimg.com/80/v2-f95d4caccca47b36a6e320f3291ec66c_hd.jpeg "Viterbi algorithm: with the hidden Markov model, this algorithm finds the optimal hidden state sequence of the observation sequence.")

#3. File Usage Explaination
##folders
1. matlab   stores plain text, code for matlab, matrix in matlab format.
2. pku_dic  stores the Chinese character dictionary text file, the character sequence in this file is identical to the emission matrix column sequence, and dictionary size is 4700 for pku_training@ICWS2005.  
##files
1. Matlab needs vectorized character sequence to perform calculation.
vectorizesequence.py processes pku_traing corpus file, writes Chinese character dictionary text file to pku_dic folder and replaces Chinese character with character dictionary index in pku_seg.txt file.
2. Compstates
compgoldstates.py processes pku_traing corpus file, writes corresponding state of each Chinese character to pku_state.txt file.
comphiddenstate.py use trained HMM model and Viterbi/Viterbi(-log) algorithm to process pku_traing corpus file, writes corresponding state of each Chinese character to pku_hmm_state.txt file.
3. Matlab folder stores corpus file as well as model segmentation result.
pku_train_vec_seq.txt replaced Chinese character with character dictionary index file and to be used by matlab code.
4. State folder stores generated golden states and model states.
pku_state.txt corresponding state of each Chinese character in pku_training file, 'B' for 'Beginning of a word', 'M' for 'Middle place of a word', 'E' for 'End of a word' and 'S' for 'Single character word'.
5. viterbi.py and neglogviterbi.py
viterbi.py with estimated transfer matrix and emission matrix, processes a sequence of Chinese character, gives the optimal sequence of hidden state.
neglogviterbi.py takes negative logarithm of the element to prevent float Underflow, thus Maximum likelihood turns into Minimum shortest path.
6. mattester.py     
validates the matrix file saved by matlab.
7. requirement.txt  
prepares for easy installation by `pip3 install -r requirement.txt`

#4. Discussion
讨论可以在知乎进行，[传送](https://zhuanlan.zhihu.com/p/106054580)

#5. Acknowledgement
Viterbi算法的实现参考了知乎[HMM+Viterbi(维特比算法)+最短路径分析](https://zhuanlan.zhihu.com/p/59889195)里的`3. 伪代码的和资料推荐`；  
在实现没灵感时参考了Github[jieba-viterbi](https://github.com/fxsjy/jieba/blob/master/jieba/posseg/viterbi.py)的实现；
在此向两位前辈表示感谢！