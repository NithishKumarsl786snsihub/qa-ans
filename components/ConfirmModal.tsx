"use client";

import { AlertTriangle, X } from "lucide-react";

export type ConfirmModalTone = "default" | "danger";

export type ConfirmModalProps = {
  open: boolean;
  title: string;
  message: string;
  confirmLabel?: string;
  cancelLabel?: string;
  tone?: ConfirmModalTone;
  onConfirm: () => void;
  onCancel: () => void;
};

export function ConfirmModal({
  open,
  title,
  message,
  confirmLabel = "Confirm",
  cancelLabel = "Cancel",
  tone = "default",
  onConfirm,
  onCancel
}: ConfirmModalProps) {
  if (!open) return null;

  return (
    <div className="modal-backdrop" role="presentation" onMouseDown={onCancel}>
      <section
        aria-describedby="confirm-modal-message"
        aria-labelledby="confirm-modal-title"
        aria-modal="true"
        className={`confirm-modal ${tone === "danger" ? "danger" : ""}`}
        role="dialog"
        onMouseDown={(event) => event.stopPropagation()}
      >
        <div className="confirm-modal-header">
          <span className="confirm-modal-icon" aria-hidden="true">
            <AlertTriangle size={20} />
          </span>
          <button className="icon-button" type="button" onClick={onCancel} aria-label="Close confirmation">
            <X size={18} />
          </button>
        </div>
        <h2 id="confirm-modal-title">{title}</h2>
        <p id="confirm-modal-message">{message}</p>
        <div className="confirm-modal-actions">
          <button
            className={tone === "danger" ? "danger-button" : "primary-button"}
            type="button"
            onClick={onConfirm}
          >
            {confirmLabel}
          </button>
          <button className="secondary-button" type="button" onClick={onCancel}>
            {cancelLabel}
          </button>
        </div>
      </section>
    </div>
  );
}
