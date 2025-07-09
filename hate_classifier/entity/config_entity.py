from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: Path
  bucket_file_path: str
  unzip_data_dir: str
  imbalance_data_dir: str
  raw_data_dir: str
  