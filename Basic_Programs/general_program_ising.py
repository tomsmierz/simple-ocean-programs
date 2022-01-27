# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# --------------------------------------------------------------------------#

# This program demonstrates a basic Ocean program that runs an Ising problem
# on the D-Wave QPU.

# --------------------------------------------------------------------------#

# Import the functions and packages that are used
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave_networkx as dnx
from numpy.random import default_rng
import pandas as pd
from dwave.cloud import Client

rng = default_rng()
NUM_READS = 10 #default value for chimera

client = Client.from_config()   
#print(client.get_solvers())

h_list = []
J_list = []
spins = []
energies = []

# Define the sampler that will be used to run the problem
graph = dnx.chimera_graph(12,12,4)

sampler = EmbeddingComposite(DWaveSampler(solver="DW_2000Q_6"))
for _ in range(500):
    h = {node: rng.normal(0,1) for node in graph.nodes}
    J = {edge: rng.normal(0,1) for edge in graph.edges}

        # Run the problem on the sampler and print the results
    sampleset = sampler.sample_ising(h, J,
                                        num_reads = NUM_READS,
                                        label='Chimera 2048')

    best = sampleset.first
    h_list.append(h)
    J_list.append(J)
    spins.append(best[0])
    energies.append(best[1])

d = {'h': h_list, 'J': J_list, "spin_conf": spins, "energy": energies}

df = pd.DataFrame(data=d)
df.to_csv("data/1152.csv")




