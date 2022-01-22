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

rng = default_rng()
NUM_READS = 10



for i in range(1,11):
    graph = dnx.chimera_graph(16, 16, 4)
    edge_attr = {edge: rng.normal(0, 1) for edge in graph.edges}
    external = {node: rng.normal(0, 1) for node in graph.nodes}


    # Define the sampler that will be used to run the problem
    sampler = EmbeddingComposite(DWaveSampler())

    # Run the problem on the sampler and print the results
    sampleset = sampler.sample_ising(external, edge_attr,
                                    num_reads = NUM_READS,
                                    label='Example - Simple Ocean Programs: Ising')

    df =sampleset.to_pandas_dataframe(sample_column = True)

    df["h"] = [external for _ in range(NUM_READS)]
    df["J"] = [edge_attr for _ in range(NUM_READS)]
    print(i)
    df.to_csv(f"data/128_{i}.csv")


