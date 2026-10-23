# R711ABR

## Descrição

Abrangências do Usuário - Items (Para Consulta)

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSis | String(003) | Não | Código do Módulo |
| CodSeq | Number(005,0) | Não | Código de Sequência das Abrangência |
| CodCon | Number(002,0) | Não | Código da Condição da Abrangência |
| CodCam | Number(002,0) | Não | Código do Campo com Abrangências |
| ValAbr | String(5000) | Sim | Conteúdo da Abrangência para um Determinado Campo |
| CodPer | Number(010,0) | Não | Código do Perfil |

---

## Chave Primária

- CodSis
- CodSeq
- CodCon
- CodCam
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R711ABR_001

**Tabela:** R710ABR

| Origem | Destino |
|--------|---------|
| CodSis | CodSis |
| CodSeq | CodSeq |

