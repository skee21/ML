import pandas as pd
filename=input("Enter Filename:")
data=pd.read_csv(filename)
concepts=data.iloc[:,:-1].values
target=data.iloc[:,-1].values
print("Applying Candidate Elimination Algorithm:")
print("Step 1 Initialize General and Specific Attributes")
def learn(concepts,target):
    specific_h=['ø']*len(concepts[0])
    general_h=[['?']*len(concepts[0])]
    print("Initial Specific Hypothesis:")
    print(specific_h)
    print("\n Initial General Hypothesis:")
    for g in general_h:
        print(g)
    for i,instance in enumerate(concepts):
        if target[i].lower()=="yes":
            print(f"\n Instance {i+1} is Positive: {instance}")
            if specific_h[0]=='ø':
                specific_h=list(instance)
            else:
                for attr in range(len(specific_h)):
                    if specific_h[attr]!=instance[attr]:
                        specific_h[attr]='?'
            general_h=[g for g in general_h
                       if all(g[j]=='?' or
                              g[j]==instance[j] or
                              specific_h[j]=='?'
                              for j in range(len(specific_h)))]
        else:
            print(f"\nInstance {i+1} is Negative: {instance}")
            new_general=[]
            for g in general_h:
                for attr in range(len(specific_h)):
                    if(specific_h[attr] !='?' and
                       specific_h[attr] !='ø' and
                       specific_h[attr] !=instance[attr]):
                        new_h=g.copy()
                        new_h[attr]=specific_h[attr]
                        if new_h not in new_general:
                            new_general.append(new_h)
            general_h=new_general
        print(f"\nSpecific Hypothesis after instance {i+1}:")
        print(specific_h)
        print(f"\nGeneral Hypothesis after instance {i+1}:")
        if len(general_h)==0:
            print("[]")
        else:
            for g in general_h:
                print(g)
    return specific_h,general_h
s_final,g_final =learn(concepts,target)
print("\nThe Maximally Specific Hypothesis is:")
print(s_final)
print("\nThe Maximally General Hypothesis is:")
if len(g_final)==0:
        print("[]")
else:
    for g in g_final:
        print(g)
