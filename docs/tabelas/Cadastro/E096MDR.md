# E096MDR

## Descrição

Tabelas - Controle de Modelos de Relatórios

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IdeMdr | String(010) | Não | Código de identificador de modelos de relatórios |
| SeqMdr | Number(002,0) | Não | Sequência do modelo de relatório |
| CodMdr | String(012) | Sim | Código do modelo do relatório |
| DesMdr | String(060) | Sim | Descrição do modelo de relatório |
| ObsMdr | String(250) | Sim | Texto da observação do modelo de relatório |
| SitReg | String(001) | Não | Situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- IdeMdr
- SeqMdr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E096MDR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

