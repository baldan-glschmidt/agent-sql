# E098LOG

## Descrição

Tabelas - Identificador de Ponto de Regras/Personalização - Log's

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| ModSis | String(003) | Não | Código da área ou gestão do sistema |
| IdeReg | String(010) | Não | Código identificador |
| CodTns | String(005) | Não | Código da transação que a regra esta associada |
| SeqReg | Number(006,0) | Não | Sequência das regras |
| DesReg | String(060) | Sim | Descrição da identificação |
| CodReg | Number(004,0) | Sim | Código da regra |
| ObsReg | String(250) | Sim | Observação do identificador |
| SitReg | String(001) | Não | Situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- ModSis
- IdeReg
- CodTns
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E098LOG_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

