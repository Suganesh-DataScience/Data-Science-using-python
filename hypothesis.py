{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"D:\\data science lap\\engineering.csv\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>institute_id</th>\n",
       "      <th>name</th>\n",
       "      <th>tlr</th>\n",
       "      <th>rpc</th>\n",
       "      <th>go</th>\n",
       "      <th>oi</th>\n",
       "      <th>perception</th>\n",
       "      <th>city</th>\n",
       "      <th>state</th>\n",
       "      <th>rank</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IR-E-U-0456</td>\n",
       "      <td>Indian Institute of Technology Madras</td>\n",
       "      <td>95.42</td>\n",
       "      <td>94.64</td>\n",
       "      <td>83.90</td>\n",
       "      <td>61.31</td>\n",
       "      <td>100.00</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>Tamil Nadu</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>IR-E-I-1074</td>\n",
       "      <td>Indian Institute of Technology Delhi</td>\n",
       "      <td>90.79</td>\n",
       "      <td>96.15</td>\n",
       "      <td>80.36</td>\n",
       "      <td>64.81</td>\n",
       "      <td>94.46</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>IR-E-U-0306</td>\n",
       "      <td>Indian Institute of Technology Bombay</td>\n",
       "      <td>91.00</td>\n",
       "      <td>93.37</td>\n",
       "      <td>77.60</td>\n",
       "      <td>49.99</td>\n",
       "      <td>92.51</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>Maharashtra</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>IR-E-I-1075</td>\n",
       "      <td>Indian Institute of Technology Kanpur</td>\n",
       "      <td>86.22</td>\n",
       "      <td>82.08</td>\n",
       "      <td>88.44</td>\n",
       "      <td>54.21</td>\n",
       "      <td>85.78</td>\n",
       "      <td>Kanpur</td>\n",
       "      <td>Uttar Pradesh</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>IR-E-U-0573</td>\n",
       "      <td>Indian Institute of Technology Kharagpur</td>\n",
       "      <td>77.32</td>\n",
       "      <td>87.11</td>\n",
       "      <td>83.21</td>\n",
       "      <td>56.62</td>\n",
       "      <td>89.31</td>\n",
       "      <td>Kharagpur</td>\n",
       "      <td>West Bengal</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  institute_id                                      name    tlr    rpc     go  \\\n",
       "0  IR-E-U-0456     Indian Institute of Technology Madras  95.42  94.64  83.90   \n",
       "1  IR-E-I-1074      Indian Institute of Technology Delhi  90.79  96.15  80.36   \n",
       "2  IR-E-U-0306     Indian Institute of Technology Bombay  91.00  93.37  77.60   \n",
       "3  IR-E-I-1075     Indian Institute of Technology Kanpur  86.22  82.08  88.44   \n",
       "4  IR-E-U-0573  Indian Institute of Technology Kharagpur  77.32  87.11  83.21   \n",
       "\n",
       "      oi  perception       city          state  rank  \n",
       "0  61.31      100.00    Chennai     Tamil Nadu     1  \n",
       "1  64.81       94.46  New Delhi          Delhi     2  \n",
       "2  49.99       92.51     Mumbai    Maharashtra     3  \n",
       "3  54.21       85.78     Kanpur  Uttar Pradesh     4  \n",
       "4  56.62       89.31  Kharagpur    West Bengal     5  "
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "tl=data.tlr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "#T-TEST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import ttest_1samp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "tl_mean=np.mean(tl)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "59.050149999999974\n"
     ]
    }
   ],
   "source": [
    "print(tl_mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "tset,t=ttest_1samp(tl,50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.631487604929007e-27\n"
     ]
    }
   ],
   "source": [
    "print(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "we reject null hypothesis\n"
     ]
    }
   ],
   "source": [
    "if t<0.05:\n",
    "   print(\"we reject null hypothesis\")\n",
    "else:\n",
    " print(\"we accept  null hypothesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Z-TEST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import stats\n",
    "from statsmodels.stats import weightstats as stests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "ztest,z=stests.ztest(tl, x2=None, value=50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.9505675759157373e-36\n"
     ]
    }
   ],
   "source": [
    "print(float(z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "we reject null hypothesis\n"
     ]
    }
   ],
   "source": [
    "if z<0.05:\n",
    "    print(\"we reject null hypothesis\")\n",
    "else:\n",
    "    print(\"we accept null hypothesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [],
   "source": [
    "#ANOVA TEST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_anova = data[['tlr','rpc']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "rp = pd.unique(data.rpc.values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [],
   "source": [
    "a={rps:data['tlr'][df_anova.rpc == rps] for rps in rp}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{94.64: 0    95.42\n",
      "Name: tlr, dtype: float64, 96.15: 1    90.79\n",
      "Name: tlr, dtype: float64, 93.37: 2    91.0\n",
      "Name: tlr, dtype: float64, 82.08: 3    86.22\n",
      "Name: tlr, dtype: float64, 87.11: 4    77.32\n",
      "Name: tlr, dtype: float64, 76.57: 5    77.21\n",
      "Name: tlr, dtype: float64, 70.73: 6    83.04\n",
      "Name: tlr, dtype: float64, 52.47: 7    82.51\n",
      "Name: tlr, dtype: float64, 50.04: 8    72.11\n",
      "Name: tlr, dtype: float64, 53.31: 9    79.89\n",
      "Name: tlr, dtype: float64, 47.77: 10    72.34\n",
      "Name: tlr, dtype: float64, 63.12: 11    64.02\n",
      "Name: tlr, dtype: float64, 46.03: 12    68.93\n",
      "Name: tlr, dtype: float64, 54.07: 13    64.62\n",
      "Name: tlr, dtype: float64, 64.06: 14    56.79\n",
      "Name: tlr, dtype: float64, 57.82: 15    64.38\n",
      "Name: tlr, dtype: float64, 62.04: 16    53.73\n",
      "Name: tlr, dtype: float64, 54.04: 17    68.13\n",
      "Name: tlr, dtype: float64, 38.12: 18    73.38\n",
      "Name: tlr, dtype: float64, 56.76: 19    65.77\n",
      "Name: tlr, dtype: float64, 47.62: 20    69.57\n",
      "Name: tlr, dtype: float64, 37.17: 21    77.05\n",
      "Name: tlr, dtype: float64, 31.3: 22    71.05\n",
      "Name: tlr, dtype: float64, 34.55: 23    83.76\n",
      "Name: tlr, dtype: float64, 30.54: 24    79.11\n",
      "Name: tlr, dtype: float64, 39.24: 25    78.2\n",
      "Name: tlr, dtype: float64, 45.19: 26    67.7\n",
      "Name: tlr, dtype: float64, 48.11: 27    63.16\n",
      "Name: tlr, dtype: float64, 47.65: 28    65.95\n",
      "Name: tlr, dtype: float64, 34.87: 29    61.95\n",
      "Name: tlr, dtype: float64, 36.8: 30    70.38\n",
      "Name: tlr, dtype: float64, 50.11: 31    71.22\n",
      "Name: tlr, dtype: float64, 24.02: 32    78.65\n",
      "Name: tlr, dtype: float64, 29.41: 33    74.73\n",
      "Name: tlr, dtype: float64, 41.69: 34    71.41\n",
      "Name: tlr, dtype: float64, 31.12: 35    63.36\n",
      "Name: tlr, dtype: float64, 33.81: 36    73.13\n",
      "Name: tlr, dtype: float64, 34.81: 37    70.07\n",
      "Name: tlr, dtype: float64, 45.83: 38    70.58\n",
      "Name: tlr, dtype: float64, 41.64: 39    63.85\n",
      "Name: tlr, dtype: float64, 41.96: 40    61.27\n",
      "Name: tlr, dtype: float64, 25.8: 41    66.08\n",
      "Name: tlr, dtype: float64, 36.66: 42    53.01\n",
      "Name: tlr, dtype: float64, 31.1: 43    66.01\n",
      "Name: tlr, dtype: float64, 24.86: 44    70.32\n",
      "Name: tlr, dtype: float64, 35.41: 45    61.63\n",
      "Name: tlr, dtype: float64, 36.98: 46    54.76\n",
      "Name: tlr, dtype: float64, 30.56: 47    59.71\n",
      "Name: tlr, dtype: float64, 19.73: 48    69.35\n",
      "Name: tlr, dtype: float64, 21.89: 49    61.94\n",
      "Name: tlr, dtype: float64, 31.77: 50    59.06\n",
      "Name: tlr, dtype: float64, 25.99: 51    66.18\n",
      "Name: tlr, dtype: float64, 26.19: 52    67.71\n",
      "Name: tlr, dtype: float64, 31.2: 53    57.49\n",
      "Name: tlr, dtype: float64, 30.98: 54    66.34\n",
      "Name: tlr, dtype: float64, 29.8: 55    55.18\n",
      "Name: tlr, dtype: float64, 29.24: 56    71.72\n",
      "Name: tlr, dtype: float64, 28.57: 57    70.69\n",
      "Name: tlr, dtype: float64, 13.98: 58    65.53\n",
      "Name: tlr, dtype: float64, 18.42: 59    68.66\n",
      "Name: tlr, dtype: float64, 20.64: 60    66.27\n",
      "Name: tlr, dtype: float64, 17.63: 61     59.63\n",
      "136    59.28\n",
      "Name: tlr, dtype: float64, 32.96: 62    64.43\n",
      "Name: tlr, dtype: float64, 18.32: 63    59.67\n",
      "Name: tlr, dtype: float64, 28.36: 64    52.55\n",
      "Name: tlr, dtype: float64, 6.8: 65     64.22\n",
      "162    49.15\n",
      "Name: tlr, dtype: float64, 24.26: 66    58.88\n",
      "Name: tlr, dtype: float64, 14.2: 67    55.66\n",
      "Name: tlr, dtype: float64, 10.04: 68    65.32\n",
      "Name: tlr, dtype: float64, 13.29: 69    63.06\n",
      "Name: tlr, dtype: float64, 11.04: 70    57.29\n",
      "Name: tlr, dtype: float64, 43.55: 71    40.82\n",
      "Name: tlr, dtype: float64, 11.92: 72    62.07\n",
      "Name: tlr, dtype: float64, 5.41: 73    70.18\n",
      "Name: tlr, dtype: float64, 21.55: 74    57.69\n",
      "Name: tlr, dtype: float64, 22.68: 75    49.6\n",
      "Name: tlr, dtype: float64, 18.33: 76    57.39\n",
      "Name: tlr, dtype: float64, 18.63: 77    69.41\n",
      "Name: tlr, dtype: float64, 12.85: 78    56.64\n",
      "Name: tlr, dtype: float64, 20.5: 79    56.5\n",
      "Name: tlr, dtype: float64, 30.89: 80    45.42\n",
      "Name: tlr, dtype: float64, 11.35: 81    63.11\n",
      "Name: tlr, dtype: float64, 4.26: 82    62.69\n",
      "Name: tlr, dtype: float64, 4.74: 83    64.38\n",
      "Name: tlr, dtype: float64, 10.39: 84    59.37\n",
      "Name: tlr, dtype: float64, 32.31: 85    46.4\n",
      "Name: tlr, dtype: float64, 15.2: 86    58.12\n",
      "Name: tlr, dtype: float64, 4.28: 87    60.88\n",
      "Name: tlr, dtype: float64, 12.89: 88    58.7\n",
      "Name: tlr, dtype: float64, 6.88: 89    64.87\n",
      "Name: tlr, dtype: float64, 13.44: 90    60.33\n",
      "Name: tlr, dtype: float64, 16.6: 91    52.49\n",
      "Name: tlr, dtype: float64, 5.07: 92    59.49\n",
      "Name: tlr, dtype: float64, 12.2: 93    57.56\n",
      "Name: tlr, dtype: float64, 24.09: 94    57.7\n",
      "Name: tlr, dtype: float64, 19.39: 95    50.85\n",
      "Name: tlr, dtype: float64, 10.41: 96    58.25\n",
      "Name: tlr, dtype: float64, 22.62: 97    45.32\n",
      "Name: tlr, dtype: float64, 3.35: 98    54.62\n",
      "Name: tlr, dtype: float64, 17.51: 99    45.99\n",
      "Name: tlr, dtype: float64, 18.31: 100    49.72\n",
      "Name: tlr, dtype: float64, 7.89: 101    61.29\n",
      "Name: tlr, dtype: float64, 15.69: 102    42.8\n",
      "Name: tlr, dtype: float64, 31.0: 103    68.53\n",
      "Name: tlr, dtype: float64, 9.94: 104    53.25\n",
      "Name: tlr, dtype: float64, 4.51: 105    62.19\n",
      "Name: tlr, dtype: float64, 11.96: 106    59.79\n",
      "Name: tlr, dtype: float64, 6.36: 107    57.03\n",
      "Name: tlr, dtype: float64, 2.33: 108    54.68\n",
      "Name: tlr, dtype: float64, 13.94: 109    54.88\n",
      "Name: tlr, dtype: float64, 10.86: 110    47.25\n",
      "Name: tlr, dtype: float64, 22.22: 111    53.75\n",
      "Name: tlr, dtype: float64, 5.29: 112    60.35\n",
      "Name: tlr, dtype: float64, 5.26: 113    55.94\n",
      "Name: tlr, dtype: float64, 18.76: 114    48.53\n",
      "Name: tlr, dtype: float64, 13.41: 115    57.31\n",
      "Name: tlr, dtype: float64, 23.49: 116    49.08\n",
      "Name: tlr, dtype: float64, 8.03: 117    59.21\n",
      "Name: tlr, dtype: float64, 19.97: 118    51.53\n",
      "Name: tlr, dtype: float64, 6.39: 119    60.17\n",
      "Name: tlr, dtype: float64, 3.72: 120    53.96\n",
      "Name: tlr, dtype: float64, 15.73: 121    55.46\n",
      "Name: tlr, dtype: float64, 8.72: 122    62.25\n",
      "Name: tlr, dtype: float64, 2.01: 123    57.82\n",
      "Name: tlr, dtype: float64, 7.74: 124    53.58\n",
      "Name: tlr, dtype: float64, 6.69: 125    51.56\n",
      "Name: tlr, dtype: float64, 6.38: 126    62.78\n",
      "Name: tlr, dtype: float64, 6.1: 127    58.44\n",
      "Name: tlr, dtype: float64, 7.54: 128    58.78\n",
      "Name: tlr, dtype: float64, 3.41: 129    54.57\n",
      "Name: tlr, dtype: float64, 10.82: 130    53.9\n",
      "Name: tlr, dtype: float64, 3.86: 131    55.76\n",
      "Name: tlr, dtype: float64, 5.43: 132    58.73\n",
      "Name: tlr, dtype: float64, 7.55: 133    56.16\n",
      "Name: tlr, dtype: float64, 5.76: 134    58.13\n",
      "Name: tlr, dtype: float64, 8.11: 135    56.85\n",
      "Name: tlr, dtype: float64, 4.32: 137    60.56\n",
      "Name: tlr, dtype: float64, 9.68: 138    46.65\n",
      "Name: tlr, dtype: float64, 8.58: 139    51.75\n",
      "Name: tlr, dtype: float64, 1.21: 140    57.68\n",
      "Name: tlr, dtype: float64, 5.15: 141    54.46\n",
      "Name: tlr, dtype: float64, 4.18: 142    57.23\n",
      "Name: tlr, dtype: float64, 24.72: 143    41.84\n",
      "Name: tlr, dtype: float64, 9.76: 144    64.04\n",
      "Name: tlr, dtype: float64, 8.13: 145    42.33\n",
      "Name: tlr, dtype: float64, 0.71: 146    59.25\n",
      "Name: tlr, dtype: float64, 2.27: 147    54.46\n",
      "Name: tlr, dtype: float64, 12.43: 148    49.09\n",
      "Name: tlr, dtype: float64, 6.12: 149    53.05\n",
      "Name: tlr, dtype: float64, 5.17: 150    56.06\n",
      "Name: tlr, dtype: float64, 4.37: 151    51.06\n",
      "Name: tlr, dtype: float64, 27.73: 152    42.43\n",
      "Name: tlr, dtype: float64, 4.9: 153    52.26\n",
      "Name: tlr, dtype: float64, 2.25: 154    54.27\n",
      "Name: tlr, dtype: float64, 5.36: 155    55.02\n",
      "Name: tlr, dtype: float64, 16.75: 156    41.49\n",
      "Name: tlr, dtype: float64, 8.29: 157    54.89\n",
      "Name: tlr, dtype: float64, 1.88: 158    47.89\n",
      "Name: tlr, dtype: float64, 6.81: 159    53.65\n",
      "Name: tlr, dtype: float64, 1.91: 160    62.29\n",
      "Name: tlr, dtype: float64, 1.4: 161    56.79\n",
      "Name: tlr, dtype: float64, 2.86: 163    57.13\n",
      "Name: tlr, dtype: float64, 6.45: 164    47.21\n",
      "Name: tlr, dtype: float64, 2.31: 165    59.15\n",
      "Name: tlr, dtype: float64, 14.26: 166    48.86\n",
      "Name: tlr, dtype: float64, 4.15: 167    50.11\n",
      "Name: tlr, dtype: float64, 4.04: 168    48.02\n",
      "Name: tlr, dtype: float64, 7.28: 169    50.61\n",
      "Name: tlr, dtype: float64, 2.84: 170    51.95\n",
      "Name: tlr, dtype: float64, 2.72: 171    53.11\n",
      "Name: tlr, dtype: float64, 2.95: 172    50.8\n",
      "Name: tlr, dtype: float64, 4.1: 173    51.95\n",
      "Name: tlr, dtype: float64, 2.65: 174    51.97\n",
      "Name: tlr, dtype: float64, 4.91: 175    56.18\n",
      "Name: tlr, dtype: float64, 11.97: 176    49.08\n",
      "Name: tlr, dtype: float64, 14.19: 177    50.08\n",
      "Name: tlr, dtype: float64, 2.66: 178    52.9\n",
      "Name: tlr, dtype: float64, 1.44: 179    56.55\n",
      "Name: tlr, dtype: float64, 7.56: 180    48.34\n",
      "Name: tlr, dtype: float64, 7.8: 181    35.51\n",
      "190    43.74\n",
      "Name: tlr, dtype: float64, 15.84: 182    47.49\n",
      "Name: tlr, dtype: float64, 1.24: 183    54.06\n",
      "Name: tlr, dtype: float64, 3.96: 184    55.12\n",
      "Name: tlr, dtype: float64, 1.11: 185    55.66\n",
      "Name: tlr, dtype: float64, 0.75: 186    48.8\n",
      "Name: tlr, dtype: float64, 1.69: 187    54.28\n",
      "Name: tlr, dtype: float64, 5.99: 188    53.98\n",
      "Name: tlr, dtype: float64, 1.15: 189    53.11\n",
      "Name: tlr, dtype: float64, 2.8: 191    48.89\n",
      "Name: tlr, dtype: float64, 2.29: 192    49.4\n",
      "Name: tlr, dtype: float64, 12.14: 193    41.95\n",
      "Name: tlr, dtype: float64, 13.82: 194    41.05\n",
      "Name: tlr, dtype: float64, 1.66: 195    49.69\n",
      "Name: tlr, dtype: float64, 7.36: 196    46.11\n",
      "Name: tlr, dtype: float64, 3.82: 197    53.6\n",
      "Name: tlr, dtype: float64, 0.46: 198    49.16\n",
      "Name: tlr, dtype: float64, 9.06: 199    50.56\n",
      "Name: tlr, dtype: float64}\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "F, p = stats.f_oneway(data['tlr'],data['rpc'],data['go'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4515521447005568e-120\n"
     ]
    }
   ],
   "source": [
    "print(p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "we reject null hypothesis\n"
     ]
    }
   ],
   "source": [
    "if p<0.05:\n",
    "    print(\"we reject null hypothesis\")\n",
    "else:\n",
    "    print(\"we accept null hypothesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Chi –square Test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import chi2_contingency"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "r_p=data.rpc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "chi = [tl[0:100],r_p[0:100]]\n",
    "stat, p_chi, dof, expected = chi2_contingency(chi) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.2482361002521188e-80\n"
     ]
    }
   ],
   "source": [
    "print(p_chi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rpc is depend on tlr\n"
     ]
    }
   ],
   "source": [
    "if p_chi<0.05:\n",
    "    print(\"rpc is depend on tlr\")\n",
    "else:\n",
    "    print(\"rpc is independent on tlr\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
