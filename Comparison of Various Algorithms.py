{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x22ab6234910>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "data = pd.read_csv('D:\\data science lap\\engineering.csv')\n",
    " \n",
    "xaxis = ['50<tlr','60<tlr', '70<trl']\n",
    "yaxis = [0,0,0]\n",
    " \n",
    "for label,row in data.iterrows():\n",
    "  if row[\"tlr\"] <=50 and row[\"oi\"]<=50:\n",
    "    yaxis[0]+=1\n",
    "  elif row[\"tlr\"] in range(50,70) and row[\"oi\"] in range(50,70):\n",
    "    yaxis[1]+=1\n",
    "  elif row[\"tlr\"] in range(70,100) and row[\"oi\"] in range(70,100):\n",
    "    yaxis[2]+=1\n",
    "\n",
    "plt.scatter(xaxis,yaxis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "probability of best oucoming 0.16363636363636364\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "output=0\n",
    "outcome=0\n",
    "heart_data=pd.read_csv('D:\\data science lap\\engineering.csv')\n",
    "for label,row in heart_data.iterrows():\n",
    "    if(row['tlr']>=50):\n",
    "        output= output+1\n",
    "    if(row['oi']>=50 and row['tlr']>=70):\n",
    "        outcome=outcome+1       \n",
    "print(\"probability of best oucoming\",outcome/output)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "probability of the best colleges:  0.3333333333333333\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "output=0\n",
    "best_clg=0\n",
    "heart_data=pd.read_csv('D:\\data science lap\\engineering.csv')\n",
    "for label,row in heart_data.iterrows():\n",
    "    if(row['go']>=50):\n",
    "        output = output+1\n",
    "    if(row['rank']<=50 and row['go']>=50):\n",
    "        best_clg =best_clg+1   \n",
    "print(\"probability of the best colleges: \",best_clg/output)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ELCOT\\anaconda3\\lib\\site-packages\\seaborn\\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='oi', ylabel='Density'>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 792x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "dataprob = pd.read_csv('D:\\data science lap\\engineering.csv')\n",
    "plt.rcParams['figure.figsize'] = (11, 4)\n",
    "plt.style.use('fivethirtyeight')\n",
    "sns.distplot(dataprob['oi'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sample mean: 51.58245\n",
      "output of the clg- mean: 51.87369999999998\n",
      "z-critical value:  1.6448536269514722\n",
      "Confidence interval: (51.440435584280465, 53.03466441571953)\n",
      "True mean: 51.87369999999998\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.random.seed(6)\n",
    "sample_chance=np.random.choice(a= heart_data['oi'], size=200)\n",
    "print (\"Sample mean:\", sample_chance.mean() )\n",
    "print(\"output of the clg- mean:\", heart_data['oi'].mean())\n",
    "import scipy.stats as stats\n",
    "import math\n",
    "np.random.seed(10)\n",
    "sample_size = 200\n",
    "sample = np.random.choice(a= heart_data['oi'],size = sample_size)\n",
    "sample_mean = sample.mean()\n",
    "z_critical = stats.norm.ppf(q = 0.95)\n",
    "print(\"z-critical value: \",z_critical)\n",
    "pop_stdev = heart_data['oi'].std()\n",
    "margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))\n",
    "confidence_interval = (sample_mean - margin_of_error,sample_mean +\n",
    "margin_of_error)\n",
    "print(\"Confidence interval:\",end=\" \")\n",
    "print(confidence_interval)\n",
    "print(\"True mean: {}\".format(heart_data['oi'].mean()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Z-statistic is :3.350156876764485\n",
      "P-value is :0.0008076580420355047\n"
     ]
    }
   ],
   "source": [
    "from statsmodels.stats.weightstats import ztest\n",
    "z_statistic, p_value = ztest(x1 = heart_data[heart_data['rpc']>=70]['oi'],value = heart_data['oi'].mean())\n",
    "print('Z-statistic is :{}'.format(z_statistic))\n",
    "print('P-value is :{}'.format(p_value))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Z-statistic is :5.86484837293545e-14\n",
      "P-value is :0.9999999999999533\n"
     ]
    }
   ],
   "source": [
    "from statsmodels.stats.weightstats import ztest\n",
    "z_statistic, p_value = ztest(x1 = heart_data[heart_data['go']>=1.2]['oi'],value = heart_data['oi'].mean())\n",
    "print('Z-statistic is :{}'.format(z_statistic))\n",
    "print('P-value is :{}'.format(p_value))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P value is 0.09278693990996034\n",
      "Dependent\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd \n",
    "from scipy.stats import chi2_contingency \n",
    "import matplotlib.pyplot as plt\n",
    "data2=pd.read_csv('D:\\data science lap\\engineering.csv')\n",
    "data2.describe()\n",
    "d1 = data2['tlr']\n",
    "d2 = data2['perception']\n",
    "plt.bar(d1, d2)\n",
    "df2=pd.crosstab(index=d1,columns=d2,dropna=True)\n",
    "c, p, dof, expected = chi2_contingency(df2)  \n",
    "alpha=0.5\n",
    "print(\"P value is \",end=\"\") \n",
    "print(p)\n",
    "if(p<=alpha):\n",
    "    print(\"Dependent\") \n",
    "else:\n",
    "    print(\"Independent\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_excel('D:\\data science lap\\eng.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "scrolled": true
   },
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
       "      <th>tlr</th>\n",
       "      <th>rpc</th>\n",
       "      <th>go</th>\n",
       "      <th>oi</th>\n",
       "      <th>perception</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>95.42</td>\n",
       "      <td>94.64</td>\n",
       "      <td>83.90</td>\n",
       "      <td>61.31</td>\n",
       "      <td>100.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>90.79</td>\n",
       "      <td>96.15</td>\n",
       "      <td>80.36</td>\n",
       "      <td>64.81</td>\n",
       "      <td>94.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>91.00</td>\n",
       "      <td>93.37</td>\n",
       "      <td>77.60</td>\n",
       "      <td>49.99</td>\n",
       "      <td>92.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>86.22</td>\n",
       "      <td>82.08</td>\n",
       "      <td>88.44</td>\n",
       "      <td>54.21</td>\n",
       "      <td>85.78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>77.32</td>\n",
       "      <td>87.11</td>\n",
       "      <td>83.21</td>\n",
       "      <td>56.62</td>\n",
       "      <td>89.31</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     tlr    rpc     go     oi  perception\n",
       "0  95.42  94.64  83.90  61.31      100.00\n",
       "1  90.79  96.15  80.36  64.81       94.46\n",
       "2  91.00  93.37  77.60  49.99       92.51\n",
       "3  86.22  82.08  88.44  54.21       85.78\n",
       "4  77.32  87.11  83.21  56.62       89.31"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_processed=df[['tlr','go']].values\n",
    "Y_processed = df[['rpc']].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train_processed, X_test_processed, Y_train_processed, Y_test_processed = train_test_split(X_processed, Y_processed, random_state=42,test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X_train shape (160, 2), len 160.\n",
      "X_test shape (40, 2), len 40.\n",
      "Y_train shape (160, 1), len 160.\n",
      "Y_test shape (40, 1), len 40.\n"
     ]
    }
   ],
   "source": [
    "print(\"X_train shape {}, len {}.\".format(X_train_processed.shape,len(X_train_processed)))\n",
    "print(\"X_test shape {}, len {}.\".format(X_test_processed.shape,len(X_test_processed)))\n",
    "print(\"Y_train shape {}, len {}.\".format(Y_train_processed.shape,len(Y_train_processed)))\n",
    "print(\"Y_test shape {}, len {}.\".format(Y_test_processed.shape,len(Y_test_processed)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Unknown label type: 'continuous'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-44-0c6d32c2fb9b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mb\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mList_depth\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mc\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mList_leaf_nodes\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m             \u001b[0mclf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mRandomForestClassifier\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn_estimators\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmax_depth\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmax_leaf_nodes\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_train_processed\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mY_train_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m             \u001b[0mpred\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mclf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_test_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\ensemble\\_forest.py\u001b[0m in \u001b[0;36mfit\u001b[1;34m(self, X, y, sample_weight)\u001b[0m\n\u001b[0;32m    328\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mn_outputs_\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    329\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 330\u001b[1;33m         \u001b[0my\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexpanded_class_weight\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_validate_y_class_weight\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    331\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    332\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"dtype\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mDOUBLE\u001b[0m \u001b[1;32mor\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mflags\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcontiguous\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\ensemble\\_forest.py\u001b[0m in \u001b[0;36m_validate_y_class_weight\u001b[1;34m(self, y)\u001b[0m\n\u001b[0;32m    556\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    557\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_validate_y_class_weight\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 558\u001b[1;33m         \u001b[0mcheck_classification_targets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    559\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    560\u001b[0m         \u001b[0my\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcopy\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\multiclass.py\u001b[0m in \u001b[0;36mcheck_classification_targets\u001b[1;34m(y)\u001b[0m\n\u001b[0;32m    170\u001b[0m     if y_type not in ['binary', 'multiclass', 'multiclass-multioutput',\n\u001b[0;32m    171\u001b[0m                       'multilabel-indicator', 'multilabel-sequences']:\n\u001b[1;32m--> 172\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Unknown label type: %r\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0my_type\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    173\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    174\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Unknown label type: 'continuous'"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import precision_score, recall_score\n",
    "from sklearn.metrics import f1_score\n",
    "\n",
    "List_estim=[10,100,200]\n",
    "List_depth=[2,10,15]\n",
    "List_leaf_nodes=[10,20,40]\n",
    "for a in List_estim:\n",
    "    for b in List_depth:\n",
    "        for c in List_leaf_nodes:\n",
    "            clf = RandomForestClassifier(n_estimators = a, max_depth = b, max_leaf_nodes = c).fit(X_train_processed, Y_train_processed)\n",
    "\n",
    "            pred = clf.predict(X_test_processed)\n",
    "            \n",
    "            print(\"Model parameters n_estimators:%0.0f, max_depth:%0.0f, max_leaf_nodes:%0.0f,\" % (a,b,c))\n",
    "            print('Accuracy Score : {:.2f}%'.format(clf.score(X_test_processed, Y_test_processed)*100))\n",
    "            print('\\nf1 Score : ', f1_score(Y_test_processed, pred))\n",
    "            print('\\nPrecision Score : ', precision_score(Y_test_processed, pred))\n",
    "            print('\\nRecall Score : ', recall_score(Y_test_processed, pred))\n",
    "            print('-------------------------------------' )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import scipy\n",
    "\n",
    "from scipy import stats\n",
    "from scipy.stats import norm, skew, boxcox\n",
    "from collections import Counter\n",
    "\n",
    "from sklearn.preprocessing import RobustScaler, StandardScaler\n",
    "from sklearn.metrics import mean_squared_error, confusion_matrix, accuracy_score, plot_confusion_matrix, auc\n",
    "from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone\n",
    "\n",
    "from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.ensemble import RandomForestClassifier, VotingClassifier\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.feature_selection import RFE\n",
    "#from imblearn.over_sampling import SMOTE\n",
    "\n",
    "#XGBOOST\n",
    "#from xgboost import XGBClassifier\n",
    "\n",
    "#warning\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Unknown label type: 'continuous'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-9403bc75ebf3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mlog_reg\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mLogisticRegression\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mlog_reg\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_train_processed\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mY_train_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0my_pred_log\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlog_reg\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_test_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mcm_log_reg\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconfusion_matrix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my_pred_log\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mY_test_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0macc_log_reg\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maccuracy_score\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mY_test_processed\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_pred_log\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py\u001b[0m in \u001b[0;36mfit\u001b[1;34m(self, X, y, sample_weight)\u001b[0m\n\u001b[0;32m   1343\u001b[0m                                    \u001b[0morder\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"C\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1344\u001b[0m                                    accept_large_sparse=solver != 'liblinear')\n\u001b[1;32m-> 1345\u001b[1;33m         \u001b[0mcheck_classification_targets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1346\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclasses_\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munique\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1347\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\multiclass.py\u001b[0m in \u001b[0;36mcheck_classification_targets\u001b[1;34m(y)\u001b[0m\n\u001b[0;32m    170\u001b[0m     if y_type not in ['binary', 'multiclass', 'multiclass-multioutput',\n\u001b[0;32m    171\u001b[0m                       'multilabel-indicator', 'multilabel-sequences']:\n\u001b[1;32m--> 172\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Unknown label type: %r\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0my_type\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    173\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    174\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Unknown label type: 'continuous'"
     ]
    }
   ],
   "source": [
    "log_reg = LogisticRegression()\n",
    "log_reg.fit(X_train_processed, Y_train_processed)\n",
    "y_pred_log = log_reg.predict(X_test_processed)\n",
    "cm_log_reg = confusion_matrix(y_pred_log, Y_test_processed)\n",
    "acc_log_reg = accuracy_score(Y_test_processed, y_pred_log)\n",
    "\n",
    "print(\"RESULT\")\n",
    "print(\"Logistic Regression Model Acc : \",acc_log_reg)\n",
    "print(\"Logistic Regression Model Cm : \",cm_log_reg)\n",
    "print('\\nf1 Score : ', f1_score(Y_test_processed, y_pred_log))\n",
    "print('\\nPrecision Score : ', precision_score(Y_test_processed, y_pred_log))\n",
    "print('\\nRecall Score : ', recall_score(Y_test_processed, y_pred_log))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Unknown label type: 'continuous'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-43c317490ef9>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0msvm\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mSVC\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0msvm\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_train_processed\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mY_train_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0my_pred_svm\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msvm\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_test_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mcm_svm\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconfusion_matrix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my_pred_svm\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mY_test_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0macc_svm\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maccuracy_score\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mY_test_processed\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_pred_svm\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py\u001b[0m in \u001b[0;36mfit\u001b[1;34m(self, X, y, sample_weight)\u001b[0m\n\u001b[0;32m    162\u001b[0m                                        accept_large_sparse=False)\n\u001b[0;32m    163\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 164\u001b[1;33m         \u001b[0my\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_validate_targets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    165\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    166\u001b[0m         sample_weight = np.asarray([]\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py\u001b[0m in \u001b[0;36m_validate_targets\u001b[1;34m(self, y)\u001b[0m\n\u001b[0;32m    542\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_validate_targets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    543\u001b[0m         \u001b[0my_\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcolumn_or_1d\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mwarn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 544\u001b[1;33m         \u001b[0mcheck_classification_targets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    545\u001b[0m         \u001b[0mcls\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munique\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my_\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreturn_inverse\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    546\u001b[0m         self.class_weight_ = compute_class_weight(self.class_weight,\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\multiclass.py\u001b[0m in \u001b[0;36mcheck_classification_targets\u001b[1;34m(y)\u001b[0m\n\u001b[0;32m    170\u001b[0m     if y_type not in ['binary', 'multiclass', 'multiclass-multioutput',\n\u001b[0;32m    171\u001b[0m                       'multilabel-indicator', 'multilabel-sequences']:\n\u001b[1;32m--> 172\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Unknown label type: %r\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0my_type\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    173\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    174\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Unknown label type: 'continuous'"
     ]
    }
   ],
   "source": [
    "svm = SVC()\n",
    "svm.fit(X_train_processed, Y_train_processed)\n",
    "y_pred_svm = svm.predict(X_test_processed)\n",
    "cm_svm = confusion_matrix(y_pred_svm, Y_test_processed)\n",
    "acc_svm = accuracy_score(Y_test_processed, y_pred_svm)\n",
    "print(\"RESULT\")\n",
    "print(\"SVM Model Acc : \",acc_svm)\n",
    "print(\"SVM Model Cm : \",cm_svm)\n",
    "print('\\nf1 Score : ', f1_score(Y_test_processed, y_pred_svm))\n",
    "print('\\nPrecision Score : ', precision_score(Y_test_processed, y_pred_svm))\n",
    "print('\\nRecall Score : ', recall_score(Y_test_processed, y_pred_svm))"
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
