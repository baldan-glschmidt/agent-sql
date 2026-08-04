# E084MDP

## Descrição

Cadastros - Máscara Derivação

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMdp | String(008) | Não | Código  da Máscara Derivação |
| DesMdp | String(020) | Não | Descrição da Máscara |
| AbrMdp | String(010) | Não | Abreviatura da Máscara |
| PosDer | Number(002,0) | Não | Quantidade de posições que a Derivação pode ser codificada (máximo 7) |
| SitMdp | String(001) | Não | Situação da Máscara de Derivação |
| CodReg | Number(004,0) | Sim | Código da Regra |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodMdp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
