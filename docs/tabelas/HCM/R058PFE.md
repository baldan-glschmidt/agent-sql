# R058PFE

## Descrição

Perfis de usuário para faixa de monitormento de Entradas do Quadro Sinótico

---

## Resumo

- Campos: 11
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PerId | Number(010,0) | Sim |  |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Cod. Coletor |
| EndEnt | Number(003,0) | Sim | Endereço da Entrada no Coletor |
| IniFai | Number(005,0) | Sim | Início da Faixa |
| FimFai | Number(005,0) | Sim | Fim da Faixa |
| DiaSem | Number(001,0) | Sim | Dia Semana |
| OpeUsu | Number(001,0) | Sim | Operação do Usuário |
| EnvCmd | String(001) | Sim | Envia Comando |
| LibAcc | String(001) | Sim | Libera Acesso |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |

---

## Chave Primária

Não possui.

---

## Índices

### R058PFEIndice1

**Tipo:** Não unico

Campos:
- PerId
- CodPlt
- CodRlg
- EndEnt
- IniFai
- DiaSem
- OpeUsu

---

## Relacionamentos

### IR_R058PFE_000

**Tabela:** R058PUQ

| Origem | Destino |
|--------|---------|
| PerId | PerId |

### IR_R058PFE_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058PFE_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

