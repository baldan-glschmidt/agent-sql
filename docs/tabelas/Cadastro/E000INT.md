# E000INT

## Descrição

Tabelas - Gerais - Integrações

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(001,0) | Não | Código da integração |
| NomTab | String(010) | Não | Nome da tabela que será integrada |
| SeqInt | Number(008,0) | Não | Sequência da integração |
| ChaTab | String(250) | Sim | Chave da tabela que será integrada |
| TipAlt | String(001) | Não | Tipo da operação |
| IndInt | Number(001,0) | Não | Indicativo da situação da integração |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| ObsInt | String(250) | Sim | Observação da integração |

---

## Chave Primária

- CodInt
- NomTab
- SeqInt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
