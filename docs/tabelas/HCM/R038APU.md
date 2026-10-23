# R038APU

## Descrição

Histórico de Apuração Colaborador

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| IniApu | Date | Não | Início da Apuração do Colaborador |
| UltApu | Date | Sim | Última data apurada para o Colaborador. |
| ApuPon | Number(001,0) | Sim | Tipo de Apuração para o Colaborador. |
| ConPon | Number(001,0) | Sim | Controle das marcações de ponto |
| ParPfa | String(001) | Sim | Participa do processo de acerto |
| AjuPon | String(001) | Sim | Processo de acerto - Ajusta ponto |
| AprPon | String(001) | Sim | Processo de acerto - Aprova o próprio ponto |
| ArtCLT | Number(001,0) | Sim | Artigo 62 da CLT |
| CodDSi | Number(003,0) | Sim | Código da Definição das Situações da Apuração |
| FusMar | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniApu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038APU_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

