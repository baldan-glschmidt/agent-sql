# R514QUA

## Descrição

Matriz de Gestão - Quadrantes

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Perfil do Formulário de Matriz de Gestão |
| SeqQua | Number(004,0) | Não | Define a sequência do Quadrante |
| NomQua | String(020) | Sim | Nome do quadrante na Matriz de Gestão |
| ObsQua | String(500) | Sim | Observações do quadrante na Matriz de Gestão |
| TitQua | String(060) | Sim | Define o título do quadrante na Matriz de Gestão |
| CabQua | String(060) | Sim | Define o cabeçalho do quadrante na Matriz de Gestão |
| TxtQua | String(060) | Sim | Define o texto do quadrante na Matriz de Gestão |
| RodQua | String(060) | Sim | Define o rodapé do quadrante na Matriz de Gestão |
| CorTit | String(010) | Sim | Define a cor do título do quadrante na Matriz de Gestão |
| CorQua | String(010) | Sim | Define a cor do quadrante na Matriz de Gestão |
| MetMin | Number(005,2) | Sim | Define a meta mínima de itens para o quadrante (em percentual) |
| MetMax | Number(005,2) | Sim | Define a meta máxima de itens para o quadrante (em percentual) |

---

## Chave Primária

- CodPer
- SeqQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R514QUA_000

**Tabela:** R514PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

