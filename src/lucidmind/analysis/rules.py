import numpy as np
from typing import Dict, List, Any

def analyze_rule_lifecycles(rule_lifecycles: Dict[str, Dict]) -> Dict[str, Any]:
    """
    Analyzes rule lifecycle data to find patterns.
    """
    if not rule_lifecycles:
        return {}
        
    lifespans = []
    peak_strengths = []
    deaths = 0
    
    for uid, data in rule_lifecycles.items():
        birth = data['birth_t']
        death = data['death_t']
        peak = data['peak_strength']
        
        peak_strengths.append(peak)
        
        if death is not None:
            lifespans.append(death - birth)
            deaths += 1
            
    return {
        'n_rules': len(rule_lifecycles),
        'n_deaths': deaths,
        'avg_lifespan': np.mean(lifespans) if lifespans else 0.0,
        'max_lifespan': np.max(lifespans) if lifespans else 0.0,
        'avg_peak_strength': np.mean(peak_strengths) if peak_strengths else 0.0,
        'lifespans': lifespans,
        'peak_strengths': peak_strengths
    }

def identify_successful_rules(rule_lifecycles: Dict[str, Dict], top_n: int = 5) -> List[str]:
    """
    Identifies rules with the longest lifespans or highest peak strengths.
    """
    scores = []
    for uid, data in rule_lifecycles.items():
        # Simple score: peak_strength * (lifespan if dead, or current_age if alive)
        # For simplicity, just use peak_strength for now
        scores.append((uid, data['peak_strength']))
        
    scores.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in scores[:top_n]]
