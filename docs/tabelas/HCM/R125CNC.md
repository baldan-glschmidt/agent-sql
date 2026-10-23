# R125CNC

## Descrição

Conhecimentos

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| DesCnc | String(100) | Sim | Descrição do Conhecimento |
| DesCer | String(025) | Sim | Descrição dos Certificadores |
| TesPra | Number(005,0) | Sim | Grupo de Perguntas do Teste Prático |
| TesTeo | Number(005,0) | Sim | Grupo de Perguntas do Teste Teórico |
| CodTbn | Number(003,0) | Sim | Código da Tabela de Notas |
| ValCnc | Number(003,0) | Sim | Validade do Conhecimento em Meses |
| NotMin | Number(005,2) | Sim | Nota Mínima do Conhecimento |
| PerMin | Number(005,2) | Sim | Percentual Mínimo para Certificação no Conhecimento |
| DesDet | String(1200) | Sim | Descrição detalhada do conhecimento |
| CodAva | Number(004,0) | Sim | Código da avaliação detalhada |
| ConWeb | String(001) | Sim | Considerar no preenchimento do Currículo Web |
| CodPro | Number(003,0) | Sim | Código da Tabela de Proficiência - OBSOLETO |
| NumRev | Number(006,0) | Sim | Revisão |
| USU_GrpCnc | String(004) | Sim | Grupo de Conhecimento |

---

## Chave Primária

- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R125CNC_000

**Tabela:** R125FAM

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |

