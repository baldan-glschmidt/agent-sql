# E098REG

## Descrição

Tabelas - Identificador de Ponto de Regras/Personalização

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| ModSis | String(003) | Não | Código da área ou gestão do sistema associado ao identificador |
| IdeReg | String(010) | Não | Código identificador |
| CodTns | String(005) | Não | Código da transação que a regra esta associada |
| DesReg | String(060) | Não | Descrição |
| CodReg | Number(004,0) | Sim | Código da regra |
| RegGup | Number(004,0) | Sim | Código da regra do Gestão Empresarial | GO UP |
| ObsReg | String(250) | Sim | Observação sobre o identificador |
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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
