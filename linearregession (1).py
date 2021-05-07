{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "##MACHINE LEARNING MODELS "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as pt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('D:\\data science lap\\engineering.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
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
     "execution_count": 3,
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
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "##MULTIPLE REGRESSION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "t=df[['tlr','rpc']]\n",
    "o=df.oi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(t, o)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0.3393788  -0.03244769]\n"
     ]
    }
   ],
   "source": [
    "print(model.coef_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "predict = model.predict([[80, 50]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[58.02017694]\n"
     ]
    }
   ],
   "source": [
    "print(predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "##LINEAR REGRESSION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import linear_model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=df[['tlr','oi']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=data.tlr \n",
    "y=data.oi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(200,)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape\n",
    "y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x28cdf93d1c0>"
      ]
     },
     "execution_count": 30,
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
    "pt.scatter(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
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
       "      <th>tlr</th>\n",
       "      <th>oi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>tlr</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.441925</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>oi</th>\n",
       "      <td>0.441925</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          tlr        oi\n",
       "tlr  1.000000  0.441925\n",
       "oi   0.441925  1.000000"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "##correlation cofficients\n",
    "data.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "##change to dataframe variables\n",
    "u=pd.DataFrame(data['tlr'])\n",
    "v=pd.DataFrame(data['oi'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "##build linear regression\n",
    "lm= linear_model.LinearRegression()\n",
    "model =lm.fit(u,v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.29831304]])"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([34.25827023])"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.19529783369525977"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(u,v)##evaluvate the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x28cdfd58e20>]"
      ]
     },
     "execution_count": 117,
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
    "#predict new value of the teaching learning and research\n",
    "#%matplotlip inline\n",
    "pt.xlabel('tlr',fontsize=10)\n",
    "pt.ylabel('oi',fontsize=10)\n",
    "pt.scatter(df.tlr,df.oi,color='blue',marker='.')\n",
    "pt.plot(df.tlr,model.predict(df[['tlr']]),color='red')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_processed=df[['tlr','rpc','go']].values\n",
    "Y_processed = df[['oi']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train_processed, X_test_processed, Y_train_processed, Y_test_processed = train_test_split(X_processed, Y_processed, random_state=42,test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X_train shape (160, 3), len 160.\n",
      "X_test shape (40, 3), len 40.\n",
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
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-126-891338dbafb7>:12: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  clf = RandomForestClassifier(n_estimators = a, max_depth = b, max_leaf_nodes = c).fit(X_train_processed, Y_train_processed)\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "Unknown label type: 'continuous'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-126-891338dbafb7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mb\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mList_depth\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mc\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mList_leaf_nodes\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m             \u001b[0mclf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mRandomForestClassifier\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn_estimators\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmax_depth\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmax_leaf_nodes\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_train_processed\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mY_train_processed\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m             \u001b[1;31m#pred = clf.predict(X_test_processed)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
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
    "List_estim=[10,50,100]\n",
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
