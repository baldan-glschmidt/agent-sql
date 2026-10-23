# R070TPE

## Descrição

Troca de Permissão para Colaboradores Outras Unidades

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador de Outra Unidade |
| DatIni | Date | Não | Data Inicial da Troca de Permissão |
| HorIni | Number(005,0) | Não | Hora Inicial da Troca de Permissão |
| DatFim | Date | Sim | Data Final da Troca de Permissão |
| HorFim | Number(005,0) | Sim | Hora Final da Troca de Permissão |
| CodPrm | Number(005,0) | Sim | Código da Permissão |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Troca de Permissão |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Troca de Permissão |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Troca de Permissão |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |

---

## Chave Primária

- NumEmp
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070TPE_001

**Tabela:** R070OCR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| NumCad | NumCad |

### IR_R070TPE_006

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

