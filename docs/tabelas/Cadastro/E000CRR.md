# E000CRR

## Descrição

Tabelas - Gerais - Correct Control

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerAmb | Number(002,0) | Não | Versão do ambiente |
| VerIno | Number(002,0) | Não | Versão de inovação ou conceitual |
| VerBas | Number(002,0) | Não | Versão da base de dados |
| VerCpl | Number(003,0) | Não | Versão da compilação |
| CodCrr | String(010) | Não | Código do correct executado |
| DesCrr | String(240) | Não | Descrição do correct executado |
| PerRpr | String(001) | Não | Indicativo se é permitido reprocessar |
| FinPrc | String(001) | Não | Indicativo se o processo foi finalizado/executado com sucesso |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- VerAmb
- VerIno
- VerBas
- VerCpl
- CodCrr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
