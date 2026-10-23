# USU_TCadInt

## Descrição

Cadastro de integração de visitantes

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_NumDoc | String(016) | Não | Numero Documento |
| USU_NomVis | String(080) | Sim | Nome Visitante |
| USU_NomEmp | String(060) | Sim | Nome Empresa |
| USU_NomEma | String(060) | Sim | Email Visitante |
| USU_DatInt | Date | Não | Data Integração |
| USU_ValInt | Date | Sim | Validade Integração |
| USU_NumCpf | String(011) | Sim | Numero CPF |
| USU_EnvEma | String(001) | Sim | Enviar Email |
| USU_CodInt | Number(005,0) | Não | Codigo Integração |
| USU_TipDoc | Number(001,0) | Sim | Tipo Documento |

---

## Chave Primária

- USU_DatInt
- USU_CodInt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
