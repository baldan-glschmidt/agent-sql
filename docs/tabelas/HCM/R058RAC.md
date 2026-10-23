# R058RAC

## Descrição

Cadastro de Reações do Acesso

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| TipAcc | Number(003,0) | Não | Tipo do Acesso |
| CodRac | Number(003,0) | Sim | Código da Reação |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Titular |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| CodFnc | Number(002,0) | Sim | Código da Função na Separação |
| GraImg | String(001) | Sim | Ativa Gravação da Imagem CFTV na Coleta da Marcação |
| IntGra | Number(003,0) | Sim | Intervalo em Segundos para Gravação da Imagem |

---

## Chave Primária

- CodPlt
- CodRlg
- TipAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058RAC_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058RAC_001

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

### IR_R058RAC_003

**Tabela:** R062TRE

| Origem | Destino |
|--------|---------|
| CodRac | CodRac |

