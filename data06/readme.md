# confusion matrix(sensitivity, 민감도, 재현율)

<img width="934" alt="스크린샷 2021-12-02 오후 4 40 10" src="https://user-images.githubusercontent.com/89058117/144378547-c8ac7b97-efe9-4251-9f43-d8e6bb92a2c1.png">

<img width="936" alt="스크린샷 2021-12-02 오후 4 40 17" src="https://user-images.githubusercontent.com/89058117/144378561-38096f9d-1d66-4c3e-9e42-7841705f1d27.png">

### 정밀도 (precision)
- 잘못된 Positive를 줄이는 데에 초점
- ex) 스펨메일 분류
  - 스팸을 스펨메일로 분류하지 않는 것(FN)은 큰 문제가없음
  - 스펨메일이 아닌 것을 스팸메일로 분류하면(FP) 업무 차질 발생
  - 이와 같이 FN 보단 FP를 줄이는 것이 중요한 경우 정밀도를 사용

### 재현율 (Recall)
- 잘못된 Negative를 줄이는데 초점
- ex) 악성코드 판별
  - 악성코드가 아닌데 악성코드로 분류하면(FP) 사용자가 확인하고 예외처리 하면 됨
  - 악성코드인데 악성코드가 아닌 것으로 분류하면(FN) 악성코드에 감염되어 위험노출
  - 이와 같이 FP보단 FN를 줄이는 것이 중요한 경우 재현율 사용

### F1-Score
- 정밀도와 재현율이 모두 중요한 경우

### 쓰는법
- from sklearn.metrics import f1_score, roc_auc_score
- from sklearn.metrics import precision_score, recall_score
  - print(accuracy_score(y_test, pred))
  - print(precision_score(y_test,pred))
  - print(recall_score(y_test, pred))
  - print(f1_score(y_test, pred))
  - print(roc_auc_score(y_test,pred))
