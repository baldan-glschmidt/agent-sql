# USU_Tdesint

## Descrição

Controlde de Desenhos - Distribuicao Interna

---

## Resumo

- Campos: 23
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_revdes | String(005) | Não | Revisao Desenho |
| USU_datenv | Date | Sim | Data Envio |
| USU_datret | Date | Sim | Data Retorno |
| USU_seqrev | Number(004,0) | Não | Sequencia |
| USU_tipimp | String(001) | Sim | Tipo |
| USU_codarm | Number(003,0) | Não | Codigo Armario |
| USU_codemp | Number(004,0) | Não | Empresa |
| USU_codccu | String(009) | Não | Centro de Custo |
| USU_coddes | String(014) | Não | Cod. Desenho |
| USU_numptc | Number(006,0) | Sim | Num. Protocolo |
| USU_qtdcop | Number(003,0) | Sim | Qtde Copias |
| USU_datsub | Date | Sim | Data Substituicao |
| USU_codder | String(007) | Sim | Codigo Derivacao |
| USU_UsuGer | Number(010,0) | Sim | Usuário Geração |
| USU_DatGer | Date | Sim | Data da Geração do Registro |
| USU_UsuApr | Number(010,0) | Sim | Usuário Aprovação/Aceitação |
| USU_DatApr | Date | Sim | Data Aprovação/Aceitação |
| USU_codfor | Number(009,0) | Sim | Cod. Fornecedor |
| USU_DevDes | String(001) | Sim | Devolução do desenho (S/N) |
| USU_EnvSub | Date | Sim | Data de envio Substituição |
| USU_DevSub | Date | Sim | Data de devolução Substituição |
| USU_nrocon | Number(004,0) | Sim | Numero Controle |
| USU_anocon | Number(004,0) | Sim | Ano Controle |

---

## Chave Primária

- USU_coddes
- USU_codccu
- USU_revdes
- USU_seqrev
- USU_codemp
- USU_codarm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
