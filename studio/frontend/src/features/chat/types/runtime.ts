// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

export interface InferenceParams {
  temperature: number;
  topP: number;
  topK: number;
  minP: number;
  repetitionPenalty: number;
  presencePenalty: number;
  maxSeqLength: number;
  maxTokens: number;
  systemPrompt: string;
  checkpoint: string;
}

export const DEFAULT_INFERENCE_PARAMS: InferenceParams = {
  temperature: 0.6,
  topP: 0.95,
  topK: 20,
  minP: 0.01,
  repetitionPenalty: 1.0,
  presencePenalty: 0.0,
  maxSeqLength: 4096,
  maxTokens: 8192,
  systemPrompt: "",
  checkpoint: "",
};

export interface ChatModelSummary {
  id: string;
  name: string;
  description?: string;
  isVision: boolean;
  isLora: boolean;
  isGguf?: boolean;
  isAudio?: boolean;
  audioType?: string | null;
  hasAudioInput?: boolean;
}

export interface ChatLoraSummary {
  id: string;
  name: string;
  baseModel: string;
  updatedAt?: number;
  source?: "training" | "exported";
  exportType?: "lora" | "merged" | "gguf";
}
