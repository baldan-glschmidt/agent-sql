# W000PRC

## Descrição

Tabela para manutenção de processos importados

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PROCID | Number(005,0) | Não | Identificador único do processo de workflow |
| PRCVER | Number(005,0) | Não | Versão do processo |
| PRCNAM | String(255) | Sim | Nome do processo de workflow |
| AUTHOR | Number(010,0) | Sim | Código do usuário autor do processo |
| FLENAM | String(255) | Sim | Nome do arquivo importado |
| INCDAT | Date | Sim | Data da inclusão do processo |
| INCTIM | Number(005,0) | Sim | Tempo da inclusão do processo |
| PRCDOC | String(4000) | Sim | Documentação do processo |
| PRCDAT | Image | Sim | Contém o binário do processo (zip) como foi enviado pelo developertools |

---

## Chave Primária

- PROCID
- PRCVER

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
