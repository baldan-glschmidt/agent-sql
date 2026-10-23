# R009JIP

## Descrição

Gestão de Incidentes - Cadastro de justificativa de incidente de ponto

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodJip | Number(003,0) | Não | Código da Justificativa de Incidente |
| DesJip | String(050) | Sim | Descrição da Justificativa de Incidente |
| TexJip | String(255) | Sim | Explicação da justificativa |
| ObsJip | String(001) | Sim | Observação obrigatória da justificativa |
| AnxJip | String(001) | Sim | Anexo obrigatório da justificativa |
| PagJip | String(001) | Sim | Precisa do aceite do gestor |
| CpiJip | String(001) | Sim | Considera para gerar pendência de justificativa para o incidente |

---

## Chave Primária

- CodJip

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
