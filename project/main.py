from simple_neuron import neuron
if __name__=='__main__':
    x=[[1,1,1], [1,-1,1], [-1,1,1], [-1,-1,1]]
    y=[1,-1, -1, 1]
    simp_ne=neuron()
    simp_ne.epoch=5
    simp_ne.train(x,y)
    print(simp_ne.w)
    print(simp_ne.test(2))