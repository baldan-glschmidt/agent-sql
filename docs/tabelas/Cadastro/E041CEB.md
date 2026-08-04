# E041CEB

## Descrição

Tabelas - Critérios e Endereços de Busca para Formas de Contabilização

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| OriFct | String(003) | Não | Módulo de origem da forma de contabilização |
| AnaSin | String(001) | Não | Nível da origem para forma de contabilização |
| SeqCeb | Number(006,0) | Não | Sequência do critério e endereço de busca para formas de contabilização |
| VarBas | Number(001,0) | Não | Variável base para o critério e endereço de busca |
| CriCeb | String(070) | Sim | Descrição para o usuário do critério de busca da variável base |
| EndCeb | String(250) | Sim | Endereço de busca da variável base |
| ObsCeb | String(250) | Sim | Texto da observação |
| SitReg | String(001) | Não | Situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- OriFct
- AnaSin
- SeqCeb

---

## Índices

### E041CEBIndice2

**Tipo:** Não unico

Campos:
- OriFct
- AnaSin
- SeqCeb
- VarBas

### E041CEBIndice3

**Tipo:** Não unico

Campos:
- OriFct
- SeqCeb

---

## Relacionamentos

Nenhum relacionamento cadastrado.
