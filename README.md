# football-team-optimization


 How to run

You need to have python 3 installed on your PC. To start playing, you can use the attached scripts:
## Genetic Algorithm

<ul>

<li> On Windows
  
`run.bat`
  
</li>
   
<li> On Linux 
  
`run.sh`
  
</li>
    
</ul>

or run these commands:

```
pip3 install -r requirements.txt || pip install -r requirements.txt
```
```
python3 src/main.py || python src/main.py || py src/main.py
```

## Bees Algorithm

<ul>
  
<li> On Windows
  
`run.bat bees`
  
</li>
   
<li> On Linux 
  
`run.sh bees`
  
</li>
    
</ul>

or run these commands:

```
pip3 install -r requirements.txt || pip install -r requirements.txt
```
```
python3 src/main.py bees || python src/main.py bees || py src/main.py bees
```

### In main.py it possible to change:

<ul>
  
<li> budget
  
</li>
   
<li> players_number
    
</li>

<li> integrity_factor
    
</li>  

</ul>


### In bees_algorithm.py it possible to change:

<ul>
  
<li> epochs
  
</li>
   
<li> player_swaps
    
</li>

<li> position_swaps
    
</li>  

<li> population_size
    
</li>  
  
<li> elite_bees
    
</li>  
  
<li> good_bees
    
</li>  

<li> elite_size
    
</li>  

<li> good_size
    
</li>  
  
</ul>

### In genetic_algorithm.py it possible to change:

<ul>
  
<li> EPOCHS_NUM
  
</li>
   
<li> POPULATION_LIMIT
    
</li>

<li> MUTATION_INCREASE
    
</li>  

<li> CHILDREN_NUM
    
</li>  
  
<li> CHILDREN_INCREASE
    
</li>  
  
<li> MUTATION_ITERATIONS
    
</li>  

<li> MUTATION_RATE
    
</li>  

<li> CROSSOVER_ITERATIONS
    
</li>  

<li> NO_IMPROVES
    
</li>   
</ul>

### The result is generated in the directory: players/static/result
