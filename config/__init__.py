default = {
      "lr": 0.0001,
      "batch_size": 2048,
      "microbatch": 64,
      "learning_steps": 320000,
      "log_interval": 20,
      "save_interval": 40000,
      "eval_interval": 1000,
      "ema_rate": "0.9999",
      "resume_checkpoint": "none",
      "schedule_sampler": "lossaware", 
      "diffusion_steps": 1000,          # Changed
      "noise_schedule": "sqrt",
      "timestep_respacing": "",
      "vocab": "bert",
      "use_plm_init": "no",
      "vocab_size": 729,                    # Added
      "config_name": "huggingface-config",
      "notes": "folder-notes",
      "data_dir": "datasets/ComMU-processed",
      "dataset": "dataset-name",
      "checkpoint_path": "checkpoint-path",
      "seq_len": 2096,                      # Changed
      "hidden_t_dim": 128,      # TODO 
      "hidden_dim": 8,        # TODO
      "dropout": 0.1,
      "use_fp16": False,
      "fp16_scale_growth": 0.001,
      "seed": 102,
      "gradient_clipping": -1.0,
      "weight_decay": 0.0,
      "learn_sigma": False,
      "use_kl": False,
      "predict_xstart": True,
      "rescale_timesteps": True,
      "rescale_learned_sigmas": False,
      "sigma_small": False,
      "emb_scale_factor": 1.0,
      "num_hidden_layers": 6                # Added
}