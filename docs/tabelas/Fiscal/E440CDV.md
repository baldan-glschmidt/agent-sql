# E440CDV

## Descrição

Compras - Contagens de Produtos - Divergências

---

## Resumo

- Campos: 19
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumCnt | Number(009,0) | Não | Número da contagem |
| SeqDiv | Number(009,0) | Não | Sequência da divergência na conferência |
| CodPro | String(014) | Sim | Código do produto da conferência |
| CodDer | String(007) | Sim | Código da derivação do produto da conferência |
| QtdCnt | Number(014,5) | Sim | Quantidade contada na conferência |
| QtdRec | Number(014,5) | Sim | Quantidade recebida na conferência |
| QtdDiv | Number(014,5) | Sim | Quantidade divergente na conferência |
| DesOco | String(250) | Sim | Descrição da ocorrência na conferência |
| DesMov | String(1000) | Sim | Descrição do movimento na conferência |
| SitDiv | Number(001,0) | Sim | Situação da divergência |
| MotSit | String(1000) | Sim | Motivo da situação da conferência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumCnt
- SeqDiv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
