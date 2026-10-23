# R044PJC

## Descrição

Processos Judiciais - Colaborador

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpIni | Date | Não | Competência Início |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código Evento Fixo |
| CodCrt | String(003) | Não | Característica do Evento |
| TipPro | Number(001,0) | Não | Tipo do Processo |
| CodPro | Number(009,0) | Sim | Código do Processo |
| CodSus | Number(014,0) | Não | Código Suspensão |
| CmpFim | Date | Sim | Competência Término |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpIni
- TabEve
- CodEve
- CodCrt
- TipPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044PJC_008

**Tabela:** R030PRO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPro | CodPro |

