import pandas as pd

SUBMISSION_DIR = '/mnt/c/Users/hyoja/OneDrive/문서/GitHub/Boostcamp_AI_Tech_3/level2/week11/submission_100.csv'
NEW_SUBMISSION_DIR = 'submission_100_deformed.csv'

def resize_bbox(original:tuple=(1024,1024), deformed:tuple=(512,512),submission_dir=None, new_submission_dir=None):

    x_rate = original[0]/deformed[0]
    y_rate = original[1]/deformed[1]

    sub = pd.read_csv(submission_dir)
    new_sub_predictionstring = []
    for i in sub['PredictionString']:
        temp = []
        for idx, loc in enumerate(i.split()):
            if idx%6 in [2,4]:
                temp.append(float(loc)*x_rate)
            elif idx%6 in [3,5]:
                temp.append(float(loc)*y_rate)
            elif idx%6 == 0:
                temp.append(int(loc))
            elif idx%6 == 1:
                temp.append(float(loc))
        new_sub_predictionstring.append(' '.join([str(i) for i in temp]))

    ii = list(sub['image_id'])
    answer = pd.DataFrame({'PredictionString':new_sub_predictionstring,'image_id':ii})
    answer.to_csv(new_submission_dir,index=False)


if __name__ == '__main__':
    resize_bbox(original=(1024,1024),deformed=(512,512),submission_dir=SUBMISSION_DIR,new_submission_dir=NEW_SUBMISSION_DIR)

