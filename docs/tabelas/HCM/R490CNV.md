# R490CNV

## Descrição

Registro de operações de conversão de base.

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IDOper | String(050) | Não | Código de identificação da operação. |
| DatOpe | Date | Não | Data e Hora de execução da atualização de base |
| VerCon | Number(003,0) | Não | Versão conceitual do sistema |
| VerIno | Number(003,0) | Não | Versão de Inovação do Sistema |
| VerBas | Number(003,0) | Não | Versão da Base de Dados do Sistema |
| VerBui | Number(003,0) | Não | Versão das Triggers e SP do Sistema |
| StaOpe | Number(001,0) | Não | Status de execução da operação de conversão |
| MsgErr | String(500) | Sim | Mensagem de erro na execução da operação |
| OpeDes | String(250) | Sim | Descrição do objetivo do script de atualização |
| ImpCnv | String(001) | Sim | Impacto do script |

---

## Chave Primária

- IDOper

---

## Índices

### R490CNVIndice1

**Tipo:** Não unico

Campos:
- VerCon
- VerIno
- VerBas
- VerBui

---

## Relacionamentos

Nenhum relacionamento cadastrado.
