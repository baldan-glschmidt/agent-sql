# E001TMO

## Descrição

Tabelas - Transações - Ligação Transação x Motivos de Ocorrência

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodTns | String(005) | Não | Código da transação |
| CodMot | Number(006,0) | Não | Código do motivo |
| DesMot | String(030) | Sim | Descrição do motivo da observação ou situação |
| LisMod | String(003) | Sim | Módulo pertencente da transação |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração do registro |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| SitTmo | String(001) | Não | Situação do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodTns
- CodMot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E001TMO_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

