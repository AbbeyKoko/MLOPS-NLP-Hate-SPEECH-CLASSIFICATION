from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionArtifacts:
  imbalance_data_dir: str
  raw_data_dir: str