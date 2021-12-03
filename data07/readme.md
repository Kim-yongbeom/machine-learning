# 머신러닝 미니프로젝트

![screencapture-notion-so-mini-mini-project-05929ae2eddd4be3a4e1ec57414a8343-2021-12-03-17_00_00](https://user-images.githubusercontent.com/89058117/144566731-c8eb4906-7c02-4bbd-b683-0dc9ae5d4d10.png)

### 타겟값에서 상관계수가 0.2가 넘는것들만 features로 선정
<img width="750" alt="스크린샷 2021-12-03 오후 5 05 03" src="https://user-images.githubusercontent.com/89058117/144567389-bccf2060-37c0-4deb-b725-ecdc7d1dabaf.png">

### 새로운 컬럼 생성
<img width="660" alt="스크린샷 2021-12-03 오후 5 05 16" src="https://user-images.githubusercontent.com/89058117/144567556-329ce0cd-4d24-4605-8d17-8e7829214df4.png">

### 이상치 제거 (1%, 99%)
<img width="783" alt="스크린샷 2021-12-03 오후 5 18 45" src="https://user-images.githubusercontent.com/89058117/144569087-9349ba88-86c0-4274-bcbc-d8f471f632d0.png">

### 사용된 라이브러리
- from sklearn.model_selection import train_test_split (train, test 분리)
- from sklearn.model_selection import cross_val_score (최적 모델 찾기 -> 파라미터값 default)
- from sklearn.model_selection import GridSearchCV (모델을 사용해 적합한 파라미터값 찾기)
- from sklearn.metrics import classification_report (confusion matrix(sensitivity, 민감도, 재현율)

### 모델별 파라미터 설정값
```
 model = [dt_clf, rf_clf, lr_clf, svm_svc, knn]
     pa = [{'max_depth':[2,3,5,10],
                  'min_samples_split':[2,3,5], 'min_samples_leaf':[1,5,8]},
           {'max_depth':[2,3,5,10],'min_samples_split':[2,3,5], 'min_samples_leaf':[1,5,8]},
           {'penalty':['l2', 'l1'],'C':[0.01, 0.1, 1, 1, 5, 10]},
            {'kernel': ['rbf'],'gamma': [0.00001,0.0001, 0.001, 0.01, 0.1, 1],
            {'C': [0.01, 0.1, 1, 10, 100, 1000]},
            {'n_neighbors' : list(range(1,20))}]
```

### 결과 그래프
<img width="750" alt="스크린샷 2021-12-03 오후 5 24 09" src="https://user-images.githubusercontent.com/89058117/144570377-b9a46c7d-e9ce-4ce4-8117-127e4d113dd8.png">
<img width="690" alt="스크린샷 2021-12-03 오후 5 24 17" src="https://user-images.githubusercontent.com/89058117/144570388-de31a272-b1f1-490f-a127-5d5fa7bfb103.png">

